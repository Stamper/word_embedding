<template>
    <div>
        <h3>Text item #{{ textId }}</h3>
        <p v-for="item in sentences" :key="item.id">
            <a :href="`/sentence/${item.id}`">{{ item.value }}</a>
        </p>
    </div>
</template>

<script>
    import {API_URL} from "../constants";

    export default {
        name: 'SentenceList',
        props: ['textId'],
        data() {
            return {
                sentences: [],
            };
        },
        methods: {
            getSentences() {
                fetch(`${API_URL}/text/${this.textId}`)
                    .then(r => r.json())
                    .then(r => {
                        this.sentences = r.data
                    });
            },
        },
        created() {
            this.getSentences();
        }
    }
</script>

