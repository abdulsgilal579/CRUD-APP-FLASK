function deleteNote(button) {
  const noteID = button.getAttribute('data-note-id');
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteID: noteID }),
    headers: {
      'Content-Type': 'application/json',
    },
  }).then((_res) => {
    window.location.href = '/';
  });
}
