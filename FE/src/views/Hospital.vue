"eslintConfig": {
	"rules": {
		"no-unused-vars": "off"
	}
}
<template>
<div class="hospital">
    <h1>This is a hospital page</h1>
    <v-btn icon large target="_blank">
        <v-icon large>mdi-domain</v-icon>
    </v-btn>

    <h2>Hospital {{ $route.params.id }}</h2>
</div>
</template>

<script>
export default { 
    watch: {
        '$route' (to,from) {

            console.log(from)

            if (to.params.id == null) {
                
                
                this.$router.push('/hospital/15')
            }
        }
    },
    mounted() {
        if (this.$route.params.id == null) {

            
                
                this.$router.push('/hospital/15')
        }
    }
}
</script>

