var eventTypeSelect = document.getElementById('event-type');
var eventLocationDiv = document.getElementById('event-location');
var eventUrlDiv = document.getElementById('event-url');

// Show or hide the location and URL fields based on the event type
eventTypeSelect.addEventListener('change', function() {
  if (eventTypeSelect.value === 'offline') {
    eventLocationDiv.classList.remove('hidden');
    eventUrlDiv.classList.add('hidden');
  } else if (eventTypeSelect.value === 'online') {
    eventLocationDiv.classList.add('hidden');
    eventUrlDiv.classList.remove('hidden');
  }
});

// Validate the form before submitting
var form = document.querySelector('form');
var eventNameInput = document.getElementById('event-name');
var eventDateTimeInput = document.getElementById('event-date-time');
var organizerNameInput = document.getElementById('organizer-name');
var organizerEmailInput = document.getElementById('organizer-email');
var organizerMobileInput = document.getElementById('organizer-mobile');
var organizerAddressInput = document.getElementById('organizer-address');
var seatsAvailableInput = document.getElementById('seats-available');
var errorDiv = document.getElementById('error');

form.addEventListener('submit', function(event) {
  if (!eventNameInput.value || !eventDateTimeInput.value || !organizerNameInput.value || !organizerEmailInput.value || !organizerMobileInput.value || !organizerAddressInput.value || !seatsAvailableInput.value) {
    event.preventDefault();
    errorDiv.innerHTML = 'Please fill out all required fields.';
  } else {
    errorDiv.innerHTML = '';
  }
});

