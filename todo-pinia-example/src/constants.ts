
export const BASE_URL = "http://127.0.0.1:5000/api";
export const REQUEST_TIMEOUT = 2000;

export const API = {

  GET_TODOS: "/todos", // get all todos
  POST_TODO: "/todos", // create a new todo
  DELETE_TODO: (todoId: string) => `/todo/${todoId}`,
  UPDATE_TODO: (todoId: string) => `/todo/${todoId}`,
  SEARCH_TODOS: "/todos/search"
}


export const TABS = {
  "TODO": "Todo",
  "SEARCH": "Search"
}