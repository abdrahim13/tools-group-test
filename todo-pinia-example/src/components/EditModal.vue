<template>
  <Modal :confirm-loading="loading" :visible="visible" title="Edit Todo" @ok="handleOk" @cancel="handleCancel">
    <Form>
      <Form.Item label="Text">
        <Input v-model:value="editText" />
      </Form.Item>
      <Form.Item label="Deadline">
        <DatePicker show-time v-model:value="selectedDate"></DatePicker>
      </Form.Item>
    </Form>
  </Modal>
</template>

<script setup lang="ts">
import dayjs from 'dayjs';
import { Modal, Input, DatePicker, Form } from 'ant-design-vue';
import { ref, computed, onMounted, watch } from 'vue';
import { useTodoStore } from '@/stores/todo';

const store = useTodoStore();
const editText = ref();
const selectedDate = ref(dayjs(Date.now()));
const visible = computed(() => !!store.currentEditingTodo);
const loading = ref(false);

async function handleOk() {
  console.log('Save');
  loading.value = true;
  const id = store.currentEditingTodo!.id;
  const text = editText.value;
  const deadlineDate = selectedDate.value.toISOString();
  await store.editTodo(id, text, deadlineDate);
  store.setCurrentEditingTodo(undefined);
  loading.value = false;
}

function handleCancel() {
  console.log('Cancel');
  store.setCurrentEditingTodo(undefined);
}

// when the modal is opened, set the editText to the currentEditingTodo's text
// when visible changes, run the function
onMounted(() => {
  watch(visible, (isVisible) => {
    if (isVisible) {
      editText.value = store.currentEditingTodo!.text;
      selectedDate.value = dayjs(store.currentEditingTodo!.deadlineDate);
    }
  });

  return () => {
    editText.value = '';
  };
});


</script>