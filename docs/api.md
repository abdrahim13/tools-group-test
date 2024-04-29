
# API (/api)


## Todo 
<details>
  <summary>
    <code>GET</code>/todo/{todo_id}
  </summary>

  #### Parameters
  todo_id (number) - id of the todo

  #### Response

  ```json
  {
    "id": 1,
    "text": "todo title",
    "important": true,
    "done": false,
    "createdAt": "2024-04-28T00:00:00Z",
  }
  ```
</details>


## Todo Create

<details>
  <summary>
    <code>POST</code>/todo
  </summary>
  #### Body
    
    ```json
    {
      "text": "todo title",
      "important": true,
      "done": false,
    }
    ```
</details>


## Todo Update
<details>
  <summary>
   <code>PUT</code>/todo/{todo_id}
  </summary>

  #### Parameters
  todo_id (number) - id of the todo

  #### Body
    
  ```json
    {
      "text": "todo title",
      "important": true,
      "done": false,
    }
  ```
  #### Response

  ```json
  {
    "id": 1,
    "text": "todo title",
    "important": true,
    "done": false,
    "createdAt": "2024-04-28T00:00:00Z",
  }
  ```
</details>



## Todo Delete

<details>
<summary>
<code>DELETE</code>/todo/{todo_id}
</summary>

#### Parameters
todo_id (number) - id of the todo

#### Response

```json
  true | false
```
</details>

## Todos List

<details>
<summary>
<code>GET</code>/todos
</summary>

#### Response

```json
[
  {
    "id": 1,
    "text": "todo title",
    "important": true,
    "done": false,
    "createdAt": "2024-04-28T00:00:00Z",
  },
  {
    "id": 2,
    "text": "todo title 2",
    "important": true,
    "done": true,
    "createdAt": "2024-04-29T00:00:00Z",
  }
]
```
</details>

## Todo Search
<details>
<summary>
<code>GET</code>/todos/search
</summary>

#### Parameters
text (string) - search text


#### Response

```json
[
  {
    "id": 1,
    "text": "text",
    "important": false,
    "done": false,
    "createdAt": "2024-04-28T00:00:00Z",
  },
  {
    "id": 2,
    "text": "todo title text",
    "important": false,
    "done": true,
    "createdAt": "2024-04-29T00:00:00Z",
  }
]
```
</details>

