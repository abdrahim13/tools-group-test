import { computed, ref } from 'vue';
import { defineStore } from 'pinia';
import type { ITodo } from '@/interfaces';
import { deleteTodo, getTodos, postTodo, searchTodos, updateTodo } from '@/service/todo';
import { debounce } from '@/utils/debounce';

function toggleProp(prop: 'important' | 'done', id: string, todo: ITodo) {
  return todo.id === id ? { ...todo, [prop]: !todo[prop] } : todo;
}



export const useTodoStore = defineStore('todo', () => {
  const todos = ref<ITodo[]>([]);
  const currentEditingTodo = ref<ITodo | undefined>();
  const loading = ref(false);


  function setCurrentEditingTodo(todo?: ITodo) {
    currentEditingTodo.value = todo;
  }

  async function addTodo(todo: ITodo) {
    const response = await postTodo(todo);
    todos.value.push(response.data);
  }

  async function removeTodo(id: string) {
    const response = await deleteTodo(id);
    if (!response.data) return;

    todos.value = todos.value.filter((todo: ITodo) => todo.id !== id);
  }

  async function toggleDone(id: string) {
    const todoToUpdate = todos.value.find((todo) => todo.id === id);
    if (!todoToUpdate) return;

    const response = await updateTodo(id, { done: !todoToUpdate.done });
    const success = response.data;
    if (!success) return;

    todos.value = todos.value.map((todo) => toggleProp('done', id, todo));
  }

  async function toggleImportant(id: string) {
    const todoToUpdate = todos.value.find((todo) => todo.id === id);
    if (!todoToUpdate) return;

    const response = await updateTodo(id, { important: !todoToUpdate.important });
    const success = response.data;
    if (!success) return;

    todos.value = todos.value.map((todo) => toggleProp('important', id, todo));
  }

  async function editTodo(id: string, text: string, deadlineDate: string) {
    const todoToUpdate = todos.value.find((todo) => todo.id === id);
    if (!todoToUpdate) return;

    const response = await updateTodo(id, { text, deadlineDate });
    const success = response.data;
    if (!success) return;

    todos.value = todos.value.map((todo) => (todo.id === id ? { ...todo, text, deadlineDate } : todo));
  }


  async function loadTodo() {
    loading.value = true;
    const response = await getTodos()
    todos.value = response.data;
    loading.value = false;
  }


  // Debounce the search function 
  // to avoid making too many requests
  // while the user is typing
  const searchDebounce = debounce(async (text: string) => {
    loading.value = true;
    const response = await searchTodos(text);
    todos.value = response.data;
    loading.value = false;
  })


  async function search(text: string) {
    await searchDebounce(text);
  }

  const doneTodosCount = computed(() => todos.value.filter((todo) => todo.done).length);
  const importantTodosCount = computed(() => todos.value.filter((todo) => todo.important).length);
  const activeTodosCount = computed(() => todos.value.filter((todo) => !todo.done).length);

  return {
    addTodo,
    removeTodo,
    toggleDone,
    toggleImportant,
    loadTodo,
    search,
    editTodo,
    setCurrentEditingTodo,
    doneTodosCount,
    importantTodosCount,
    activeTodosCount,
    todos,
    currentEditingTodo,
    loading,
  };
});
