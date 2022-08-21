
const addTask = async (title, listId) => {
  try {
  const res = await axios.post('/api/tasks/',
      { title, parent_list: listId },
      { headers: { 'X-CSRFToken': csrftoken }}
      );
  location.reload();
    } catch (e) {
      console.error(e);
    }
};

const removeTask = async taskId => {
  try {
  const res = await axios.delete('/api/tasks/' + taskId + '/',
      { headers: { 'X-CSRFToken': csrftoken }}
      );
  location.reload();
    } catch (e) {
      console.error(e);
    }
};

const updateTask = async (taskId, taskStatus) => {
  try {
  const res = await axios.patch('/api/tasks/' + taskId + '/',
      { id: taskId, completed: taskStatus},
      { headers: { 'X-CSRFToken': csrftoken }}
      );
  location.reload();
    } catch (e) {
      console.error(e);
    }
};
