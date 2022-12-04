// add event listeners for the create and edit form input fields
document.getElementById('create-title').addEventListener('input', handleCreateTitleInput);
document.getElementById('create-body').addEventListener('input', handleCreateBodyInput);
document.getElementById('edit-title').addEventListener('input', handleEditTitleInput);
document.getElementById('edit-body').addEventListener('input', handleEditBodyInput);

// handle the create title input event
function handleCreateTitleInput(e) {
  // get the input field
  const input = e.target;

  // check if the input is valid
  if (input.checkValidity()) {
    // if valid, hide the error message
    document.getElementById('create-title-error').style.display = 'none';
  } else {
    // if invalid, show the error message
    document.getElementById('create-title-error').style.display = 'block';
  }
}

// handle the create body input event
function handleCreateBodyInput(e) {
  // get the input field
  const input = e.target;

  // check if the input is valid
  if (input.checkValidity()) {
    // if valid, hide the error message
    document.getElementById('create-body-error').style.display = 'none';
  } else {
    // if invalid, show the error message
    document.getElementById('create-body-error').style.display = 'block';
  }
}

// handle the edit title input event
function handleEditTitleInput(e) {
  // get the input field
  const input = e.target;

  // check if the input is valid
  if (input.checkValidity()) {
    // if valid, hide the error message
    document.getElementById('edit-title-error').style.display = 'none';
  } else {
    // if invalid, show the error message
    document.getElementById('edit-title-error').style.display = 'block';
  }
}

// handle the edit body input event
function handleEditBodyInput(e) {
  // get the input field
  const input = e.target;

  // check if the input is valid
  if (input.checkValidity()) {
    // if valid, hide the error message
    document.getElementById('edit-body-error').style.display = 'none';
  } else {
    // if invalid, show the error message
    document.getElementById('edit-body-error').style.display = 'block';
  }
}
