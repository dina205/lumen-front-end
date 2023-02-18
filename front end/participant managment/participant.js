// Get the registered participants data from the server
const participants = getParticipantsData();

// Sort the participants by registration date in descending order
participants.sort((a, b) => new Date(b.registrationDate) - new Date(a.registrationDate));

// Add the participants to the table
const participantTableBody = document.getElementById('participant-table-body');
participants.forEach((participant) => {
  const row = participantTableBody.insertRow(0);
  row.insertCell(0).innerHTML = participant.name;
  row.insertCell(1).innerHTML = participant.email;
  row.insertCell(2).innerHTML = participant.phone;
  row.insertCell(3).innerHTML = participant.event;
  row.insertCell(4).innerHTML = participant.registrationDate;
  row.insertCell(5).innerHTML = '<button>Edit</button> <button>Delete</button>';
});

// Add search functionality
const searchInput = document.getElementById('search-input');
searchInput.addEventListener('input', () => {
  const searchText = searchInput.value.toLowerCase();
  participants.forEach((participant) => {
    const row = document.getElementById(`participant-${participant.id}`);
    if (row) {
      if (participant.name.toLowerCase().includes(searchText) ||
          participant.email.toLowerCase().includes(searchText)) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    }
  });
});
