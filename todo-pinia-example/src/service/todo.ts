import type { ITodo } from "@/interfaces";
import { fetcher } from "./axios";
import { API } from "../constants";




export async function getTodos() {
  const api = API.GET_TODOS;
  return await fetcher.get(api);
}


export async function postTodo(todo: ITodo) {
  const api = API.POST_TODO;
  return await fetcher.post<ITodo>(api, todo);
}


export async function updateTodo(todoId: string, todo: Partial<ITodo>) {
  const api = API.UPDATE_TODO(todoId);
  return await fetcher.put<ITodo>(api, todo);
}

export async function deleteTodo(todoId: string) {
  const api = API.DELETE_TODO(todoId);
  return await fetcher.delete<boolean>(api);
}


export async function searchTodos(text: string) {
  const api = API.SEARCH_TODOS;
  return await fetcher.get<ITodo[]>(api, {
    params: { text },
  })
}