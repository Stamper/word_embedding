<template>
    <div>
        <h3>Text items list</h3>
        <p v-for="item in textItems" :key="item.id">
            {{ item.preview }} (<a :href="`text/${item.id}`">count: {{ item.sentences }}</a>)
        </p>
        <Paginator :pages="count" basePath="/?page=" :current="page"/>
    </div>
</template>

<script>
    import {API_URL} from '../constants';
    import Paginator from '@/components/Paginator.vue';

    export default {
        name: 'TextList',
        components: {Paginator},
        data() {
            return {
                textItems: [],
                page: 0,
                count: 0
            };
        },
        methods: {
            getTextItems() {
                this.page = this.$route.query.page || 1;
                fetch(`${API_URL}/text?page=${this.page}`)
                    .then(r => r.json())
                    .then(r => {
                        this.textItems = r.data;
                        this.count = Math.ceil(r.count / 10);
                    });
            },
        },
        created() {
            this.getTextItems();
        }
    }
</script>

