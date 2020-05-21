<template>
    <p>
        <span v-for="n in pages">
            <span v-if="n == current"><{{n}}></span>
            <span v-else><a :href="`${basePath}${n}`"><{{n}}></a></span>
        </span>
    </p>
</template>

<script>
    export default {
        name: 'Paginator',
        props: ['current', 'basePath', 'pages'],
    }
</script>
