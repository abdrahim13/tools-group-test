<template>

  <Tabs defaultActiveKey="1" @change="handleTabChange">
    <TabPane :tab="TABS.TODO" :key="TABS.TODO">
      <Input v-model:value="field" class="input" @keyup.enter="handleAddTodo" placeholder="Type name of todo" />
    </TabPane>
    <TabPane :tab="TABS.SEARCH" :key="TABS.SEARCH">
      <InputSearch enter-button v-model:value="searchText" class="input" @keyup.stop="handleSearchTodo"
        placeholder="Search" />
    </TabPane>
  </Tabs>

  <Card bordered title="Todo Stats">
    <Typography>Done:
      <Badge :count="store.doneTodosCount" />
    </Typography>
    <Typography>Important:
      <Badge :count="store.importantTodosCount" />
    </Typography>
    <Typography>Active:
      <Badge :count="store.activeTodosCount" />
    </Typography>
  </Card>
  <List :loading="store.loading" class="todo-list" :data-source="store.todos">
    <template #renderItem="{ item }">
      <ListItem class="list-item" :class="{ 'important-list-item': item.important }">
        <div>
          <Button @click="store.toggleDone(item.id)" :type="item.done ? 'primary' : 'text'" class="icon">
            <template #icon>
              <CheckOutlined title="Toggle done" />
            </template>
          </Button>
          <Button @click="store.toggleImportant(item.id)" :type="item.important ? 'primary' : 'text'" class="icon">
            <template #icon>
              <ExclamationOutlined  title="Toggle important" />
            </template>
          </Button>
          <EditTwoTone class="icon" @click="() => toggleEditMode(item)" title="Edit" />
        </div>
        <div :class="{ 'line-through': item.done }">
          <Typography :class="{ 'text-bold': item.important }">{{ item.text }}</Typography>
          <p>{{ readableDate(item.deadlineDate) }}</p>
        </div>

        <CloseCircleOutlined class="icon icon-danger" @click="store.removeTodo(item.id)" />
      </ListItem>
    </template>
  </List>
  <EditModal />
</template>

<script setup lang="ts">
import type { ITodo } from '@/interfaces';
import { TABS } from '@/constants';
import { readableDate } from '@/utils/dateFormatter';
import {
  Input, List, ListItem,
  Typography, Tabs, TabPane, Card, InputSearch,
  Badge, Button
} from 'ant-design-vue';
import EditModal from './EditModal.vue';
import { ref, onMounted } from 'vue';
import { useTodoStore } from '@/stores/todo';
import CloseCircleOutlined from '@ant-design/icons-vue/lib/icons/CloseCircleOutlined';
import CheckOutlined from '@ant-design/icons-vue/lib/icons/CheckOutlined';
import ExclamationOutlined from '@ant-design/icons-vue/lib/icons/ExclamationOutlined';
import { EditTwoTone } from '@ant-design/icons-vue';
import type { Key } from 'ant-design-vue/lib/vc-tree/interface';

const field = ref('');
const searchText = ref('');
const store = useTodoStore();

function createTodo(text: string) {
  return { text, done: false, important: false } as ITodo;
}

function handleSearchTodo() {
  store.search(searchText.value);
}

function handleTabChange(key: Key) {
  if (key === TABS.TODO) {
    store.loadTodo();
  }
}

function handleAddTodo() {
  const todo = createTodo(field.value);
  store.addTodo(todo);
  field.value = '';
}

function toggleEditMode(todo?: ITodo) {
  store.setCurrentEditingTodo(todo);
}


// Load todos from database
onMounted(() => {
  store.loadTodo();
});

</script>

<style scoped>
.input {
  margin: 15px 0;
}

.icon {
  margin-right: 1rem;
  border-radius: 50%;
  padding: 0.5rem;
  cursor: pointer;
  border: 1px solid #ccc;
  font-size: 1rem;
}

.icon.icon-danger {
  color: red;
  border-color: red;
}

.todo-list {
  margin-top: 1rem;
}

.line-through {
  text-decoration: line-through;
}

.text-bold {
  font-weight: 700;
}

.important-list-item {
  background: #f0f0f0;
}

.todo-list {
  background: white;
  padding: 1rem;
}

.list-item {
  padding: 1rem;
}
</style>
@/utils/dateFormatter