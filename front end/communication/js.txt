// Get the email template element and compile the template using a template engine like Handlebars.js
const emailTemplate = document.getElementById('email-template').innerHTML;
const template = Handlebars.compile(emailTemplate);

// Get the form data for the event and participants
const eventData = getEventData();
const participants = getParticipants();

// Loop through the participants and send email notifications to each one
participants.forEach((participant) => {
  // Compile the email message using the template and participant data
  const emailData = {
    name: participant.name,
    event_name: eventData.name,
    event_date: eventData.date,
    event_time: eventData.time,
    event_location: eventData.location,
    contact_email: eventData.contact_email
  };
  const message = template(emailData);

  // Send the email using PHP and the mail() function
  const to = participant.email;
  const subject = 'Event Update';
  const headers = 'From: ' + eventData.contact_email + '\r\n' +
                  'Reply-To: ' + eventData.contact_email + '\r\n' +
                  'Content-type: text/html; charset=iso-8859-1\r\n';
  mail(to, subject, message, headers);
});
