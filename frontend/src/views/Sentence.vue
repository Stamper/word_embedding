<template>
  <div>
    <ResultList :sentenceId="sentenceId"/>
  </div>
</template>

<script>
import ResultList from '@/components/ResultList.vue'

export default {
  components: {
    ResultList
  },
  props: ['sentenceId']
}
</script>
