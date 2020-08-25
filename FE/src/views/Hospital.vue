<template>
<div class="hospital">
    <v-container>
        <v-row align="start" justify='start'>
            <v-col class="text-center">
                <div>
                    <v-bottom-navigation background-color='green' shift>
                        <v-btn>
                            <span>All Hospitals</span>
                            <v-icon>mdi-hospital-building</v-icon>
                        </v-btn>

                        <v-btn>
                            <span>Add Hospital</span>
                            <v-icon>mdi-home-plus-outline</v-icon>
                        </v-btn>
                        <v-btn>
                            <span>Edit Hospital</span>
                            <v-icon>mdi-home-edit-outline</v-icon>
                        </v-btn>
                        <v-btn>
                            <span>Remove Hospital</span>
                            <v-icon>mdi-home-remove-outline</v-icon>
                        </v-btn>

                    </v-bottom-navigation>
                </div>
            </v-col>
        </v-row>
        <v-row>
            <AllHospital />
        </v-row>

    </v-container>

</div>
</template>

<script>
 import AllHospital from "@/components/AllHospitals";

 export default {
     name: "Hospital",
     components: {
         AllHospital
     },
     watch: {
         '$route'(to, from) {

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
