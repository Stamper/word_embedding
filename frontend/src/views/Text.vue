<template>
  <div>
    <SentenceList :textId="textId"/>
  </div>
</template>

<script>
import SentenceList from '@/components/SentenceList.vue'

export default {
  components: {
    SentenceList
  },
  props: ['textId']
}
</script>
