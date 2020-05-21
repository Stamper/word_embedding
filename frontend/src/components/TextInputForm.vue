<template>
    <div>
        <h3>Add new text</h3>
        <textarea v-model="text" placeholder="insert your text here" rows="20" cols="100"></textarea>
        <br/>
        <button v-on:click="submitText">Save</button>
    </div>
</template>

<script>
    import {API_URL} from "../constants";

    export default {
        name: 'TextInputForm',
        data() {
            return {
                text: ''
            }
        },
        methods: {
            submitText() {
                fetch(`${API_URL}/text`,
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'text/plain'
                        },
                        body: this.text
                    })
                    .then(r => r.json())
                    .then(r => {
                        if (r.status == 'ok'){
                            this.$router.push({path: `/text/${r.id}`});
                        }
                    });
            }
        }
    }
</script>
