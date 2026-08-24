$(document).ready(function () {
  symptoms = JSON.parse(symptoms);
  let input = $("#message-text");
  let sendBtn = $("#send");
  let startOverBtn = $("#start-over");
  let uploadLabBtn = $("#upload-lab");
  let labFileInput = $("#lab-file-input");
  let dataList = $("#symptoms-list");
  let chat = $("#conversation");

  // Handler for any input on the message input field
  input.on("input", function () {
    let insertedValue = $(this).val();
    $("#symptoms-list").empty();

    if (insertedValue.length > 1) {
      ssymptoms = $.fn.getSuggestedSymptoms(insertedValue);
      if (ssymptoms.length === 0) {
        $(".symptoms-list-container ").slideUp();
      } else {
        for (let i = 0; i < ssymptoms.length; i++) {
          var li = document.createElement("li");
          li.textContent = ssymptoms[i];
          dataList.append(li);
        }
        $(".symptoms-list-container ").slideDown();
      }
    } else {
      $(".symptoms-list-container ").slideUp();
    }
  });

  startOverBtn.on("click", function () {
    $.fn.startOver();
  });

  sendBtn.on("click", function () {
    $.fn.handleUserMessage();
  });

  // ─── Lab Report Upload Handlers ───────────────────────────────
  uploadLabBtn.on("click", function () {
    labFileInput.trigger("click");
  });

  labFileInput.on("change", function () {
    var file = this.files[0];
    if (file) {
      $.fn.handleLabUpload(file);
      $(this).val(""); // reset so same file can be re-uploaded
    }
  });

  // Handler for click on one of the suggested symptoms
  dataList.on("click", "li", function () {
    input.val($(this).text());
    $(".symptoms-list-container ").slideUp();
  });

  input.on("blur", function () {
    $(".symptoms-list-container ").slideUp();
  });

  input.on("keypress", function (e) {
    if (e.which == 13) {
      $.fn.handleUserMessage();
    }
  });

  // Handler function for sending a message
  $.fn.handleUserMessage = function () {
    if (input.val()) {
      $.fn.appendUserMessage();
      $.fn.getPredictedSymptom();
      input.val("");
      chat.animate({
        scrollTop: $("#conversation .message-body:last-child").position().top,
      });
    }
  };

  // ─── Lab Upload Pipeline ──────────────────────────────────────
  $.fn.handleLabUpload = function (file) {
    // Show a "user attached" message
    $.fn.appendUserAttachment(file.name);

    // Show scanning animation
    $.fn.appendScanningMessage();

    var formData = new FormData();
    formData.append("lab_image", file);

    $.ajax({
      url: "/upload-lab-report",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Remove scanning animation
        $(".scanning-message").last().closest(".message-body").remove();

        if (response.success) {
          $.fn.appendLabResultsMessage(response);
        } else {
          $.fn.appendBotMessage(
            '<i class="fas fa-exclamation-triangle" style="color:#ff6b6b;"></i> ' +
              response.error
          );
        }

        chat.animate({
          scrollTop:
            $("#conversation .message-body:last-child").position().top,
        });
      },
      error: function () {
        $(".scanning-message").last().closest(".message-body").remove();
        $.fn.appendBotMessage(
          '<i class="fas fa-exclamation-triangle" style="color:#ff6b6b;"></i> Failed to process the lab report. Please try again.'
        );
      },
    });
  };

  // Show file attachment message from user
  $.fn.appendUserAttachment = function (filename) {
    var html =
      '<div class="row message-body"><div class="col-sm-12 message-main-sender"><div class="sender"><div class="message-text">' +
      '<i class="fas fa-file-image" style="margin-right:8px; color: var(--accent-cyan);"></i> Uploaded: <strong>' +
      filename +
      "</strong></div></div></div></div>";
    $("#conversation").append(html);
  };

  // Show scanning/processing animation
  $.fn.appendScanningMessage = function () {
    var html =
      '<div class="row message-body"><div class="col-sm-12 message-main-receiver"><div class="receiver scanning-message">' +
      '<div class="message-text">' +
      '<div class="scan-animation">' +
      '<div class="scan-icon"><i class="fas fa-microscope"></i></div>' +
      '<div class="scan-text">Scanning lab report<span class="dot-anim">...</span></div>' +
      '<div class="scan-bar"><div class="scan-bar-fill"></div></div>' +
      "</div></div></div></div></div>";
    $("#conversation").append(html);

    chat.animate({
      scrollTop: $("#conversation .message-body:last-child").position().top,
    });
  };

  // Render the full lab results card
  $.fn.appendLabResultsMessage = function (response) {
    var evaluated = response.evaluated;
    var derivedSymptoms = response.derived_symptoms;

    // Build the results table
    var tableHtml =
      '<div class="lab-results-card">' +
      '<div class="lab-results-header"><i class="fas fa-flask"></i> Lab Report Analysis</div>' +
      '<table class="lab-results-table">' +
      "<thead><tr><th>Marker</th><th>Value</th><th>Ref Range</th><th>Status</th></tr></thead>" +
      "<tbody>";

    for (var i = 0; i < evaluated.length; i++) {
      var e = evaluated[i];
      var statusClass = "status-normal";
      var statusIcon = "✓";
      if (e.status === "High") {
        statusClass = "status-high";
        statusIcon = "▲";
      } else if (e.status === "Low") {
        statusClass = "status-low";
        statusIcon = "▼";
      }

      tableHtml +=
        "<tr>" +
        "<td><strong>" + e.name + "</strong></td>" +
        "<td>" + e.value + " " + e.unit + "</td>" +
        "<td>" + e.ref_range + "</td>" +
        '<td class="' + statusClass + '">' + statusIcon + " " + e.status + "</td>" +
        "</tr>";
    }

    tableHtml += "</tbody></table>";

    // Show derived symptoms if any
    if (derivedSymptoms.length > 0) {
      tableHtml +=
        '<div class="lab-derived-symptoms">' +
        '<div class="derived-header"><i class="fas fa-brain"></i> Symptoms detected from lab values:</div>' +
        '<div class="derived-tags">';

      for (var j = 0; j < derivedSymptoms.length; j++) {
        tableHtml +=
          '<span class="symptom-tag">' +
          derivedSymptoms[j].replace(/_/g, " ") +
          "</span>";
      }

      tableHtml += "</div></div>";
    } else {
      tableHtml +=
        '<div class="lab-derived-symptoms">' +
        '<div class="derived-header" style="color: var(--text-secondary);">' +
        '<i class="fas fa-check-circle" style="color:#00ff88;"></i> All values appear normal — no additional symptoms flagged.</div></div>';
    }

    tableHtml +=
      '<div class="lab-results-footer">' +
      "These symptoms have been added to your session. You can continue adding more symptoms or type <strong>Done</strong> for your diagnosis." +
      "</div></div>";

    // Wrap in bot message
    var fullHtml =
      '<div class="row message-body"><div class="col-sm-12 message-main-receiver"><div class="receiver"><div class="message-text">' +
      tableHtml +
      "</div></div></div></div>";

    $("#conversation").append(fullHtml);
  };

  $.fn.startOver = function () {
    $.fn.getPredictedSymptom(true);
    $("#conversation").empty();
    const text =
      'Welcome! I\'m ai-doctor_}mihir_ahana. What symptoms are you currently experiencing? When you\'ve entered all of your symptoms, please write \'<b>Done</b>\'. Make sure you enter as much symptoms as possible so the prediction can be as correct as possible.<br><br><span class="lab-upload-hint">📎 <strong>NEW:</strong> You can also upload a photo of your lab report (blood test) and I\'ll read the numbers for you!</span>';
    $("#conversation").append(
      `<div class="row message-previous"><div class="col-sm-12 previous"></div></div><div class="row message-body"><div class="col-sm-12 message-main-receiver"><div class="receiver"><div class="message-text">${text}</div></div></div></div>`
    );
    input.val("");
  };

  // Creates the newly sent message element
  $.fn.appendUserMessage = function () {
    var text = input.val();
    $("#conversation").append(
      `<div class="row message-body"><div class="col-sm-12 message-main-sender"><div class="sender"><div class="message-text">${text}</div></div></div></div>`
    );
  };

  $.fn.appendBotMessage = function (text) {
    $("#conversation").append(
      `<div class="row message-body"><div class="col-sm-12 message-main-receiver"><div class="receiver"><div class="message-text">${text}</div></div></div></div>`
    );
  };

  // Retreives prediction to show as bot message
  $.fn.getPredictedSymptom = function (again) {
    var text = input.val();
    if (again) text = "done";

    $.ajax({
      url: "/symptom",
      data: JSON.stringify({ sentence: text }),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      type: "POST",
      success: function (response) {
        console.log("BOT RESPONSE:", response);
        if (!again) $.fn.appendBotMessage(response);
      },
      error: function () {
        console.log("ERROR:", err);
      },
    });
  };

  $.fn.getSuggestedSymptoms = function (val) {
    let suggestedSymptoms = [];
    $.each(symptoms, function (i, v) {
      if (v.includes(val)) {
        suggestedSymptoms.push(v);
      }
    });
    return suggestedSymptoms.slice(0, 3);
  };
});
