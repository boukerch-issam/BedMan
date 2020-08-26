<template>
<div class="hospital">
    <v-container>
        <v-row>
            <AllHospital />
        </v-row>
        <v-row align="end" justify='start'>
            <v-col class="text-center">
                <div>
                    <v-bottom-navigation v-model="bottomNav" background-color='green' shift grow @change="botton_nav">
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

                        <v-chip  :active= "chip">
                            {{chiptxt}}
                        </v-chip>

                    </v-bottom-navigation>
                </div>
            </v-col>
        </v-row>

    </v-container>
</div>
</template>

<script>
import AllHospital from "@/components/AllHospitals";

export default {
    name: "Hospital",
    data() {
        return {
            bottomNav: '0',
            chip: false,
            chiptxt : ''
        }
    },
    components: {
        AllHospital
    },
    methods: {
        botton_nav(e) {
            //console.log(e)
        },
        closeCurrentHospital() {
            this.chip = false
            this.$store.commit('setCurrentHospital', [])

        }
    },

    watch: {
        '$store.state.currentHospital'() {

            if (this.$store.state.currentHospital._id != null) {
                this.chip = true
                this.chiptxt='Current Hospital : '+this.$store.state.currentHospital.name
            } else {
                this.chiptxt=''
                this.chip = false
                
            }
        }

    },
    //  mounted() {
    //  if (this.$route.params.id == null) {

    //      this.$router.push('/hospital/')
    //  }

    //}
}
</script>
