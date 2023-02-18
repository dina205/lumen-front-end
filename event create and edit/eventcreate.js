// Select the form and submit button
const eventForm = document.getElementById('event-form');
const submitButton = document.getElementById('submit-event');

// Add event listener for form submission
eventForm.addEventListener('submit', function(event) {
  event.preventDefault();

  // Get form values
  const eventName = document.getElementById('event-name').value;
  const eventDate = document.getElementById('event-date').value;
  const eventLocation = document.getElementById('event-location').value;
  const eventPrice = document.getElementById('event-price').value;

  // Create a new event object
  const event = {
    name: eventName,
    date: eventDate,
    location: eventLocation,
    price: eventPrice
  };

  // Send event data to server
  fetch('/create-event', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(event)
  })
  .then(response => {
    if (response.ok) {
      alert('Event created successfully!');
      eventForm.reset();
    } else {
      alert('Error creating event!');
    }
  })
  .catch(error => {
    alert('Error creating event!');
  });
});
