const csrftoken = document.querySelector('#list-form > input').value;

const addList = async title => {
    try {
    const res = await axios.post('/api/lists/',
        { title },
        { headers: { 'X-CSRFToken': csrftoken }}
        );
    location.reload();
      } catch (e) {
        console.error(e);
      }
};

const removeList = async listId => {
    try {
    const res = await axios.delete('/api/lists/' + listId + '/',
        { headers: { 'X-CSRFToken': csrftoken }}
        );
    location.reload();
      } catch (e) {
        console.error(e);
      }
};
