<template>
    <div>
        <h3>Similar sentences for item #{{ sentenceId }}</h3>
        <div v-if="status === 'pending'">
            <p>Try again later...</p>
        </div>
        <div v-else>
            <p v-for="item in sentences" :key="item.id">
                {{ item.value }} (<a :href="`/text/${item.text_id}`">text #{{ item.text_id }}</a>)
                <span>{{item.distance}}</span>
            </p>
        </div>
    </div>
</template>

<script>
    import {API_URL} from "../constants";

    export default {
        name: 'ResultList',
        props: ['sentenceId'],
        data() {
            return {
                status: '',
                sentences: [],
            };
        },
        methods: {
            getSentences() {
                fetch(`${API_URL}/sentence/${this.sentenceId}`)
                    .then(r => r.json())
                    .then(r => {
                        this.status = r.status;
                        this.sentences = r.data || [];
                    });
            },
        },
        created() {
            this.getSentences();
        }
    }
</script>

