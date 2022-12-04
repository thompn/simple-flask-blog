// add event listeners for the create and edit form submit buttons
document.getElementById('create-form').addEventListener('submit', handleCreateFormSubmit);
document.getElementById('edit-form').addEventListener('submit', handleEditFormSubmit);

// handle the create form submit event
function handleCreateFormSubmit(e) {
  e.preventDefault();

  // get the form data
  const title = document.getElementById('create-title').value;
  const body = document.getElementById('create-body').value;

  // create a new post with the form data
  createPost(title, body);
}

// handle the edit form submit event
function handleEditFormSubmit(e) {
  e.preventDefault();

  // get the form data
  const id = document.getElementById('edit-id').value;
  const title = document.getElementById('edit-title').value;
  const body = document.getElementById('edit-body').value;

  // update the post with the form data
  updatePost(id, title, body);
}

// send an HTTP request to create a new post
function createPost(title, body) {
  const data = {
    title: title,
    body: body,
  };

  fetch('/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      // redirect to the homepage
      window.location.href = '/';
    });
}

// send an HTTP request to update an existing post
function updatePost(id, title, body) {
  const data = {
    id: id,
    title: title,
    body: body,
  };

  fetch('/edit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      // redirect to the homepage
      window.location.href = '/';
    });
}
