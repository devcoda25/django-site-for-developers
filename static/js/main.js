// Get the search form element
const searchForm = document.getElementById('search-form');

// Add an event listener to the form submission
searchForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the default form submission
  const queryInput = searchForm.querySelector('input[name="query"]');
  const query = queryInput.value.trim();
  if (query.length > 0) {
    // Submit the form programmatically
    searchForm.submit();
  }
});