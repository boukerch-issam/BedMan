<template>
<div class="hospital">
        <v-snackbar v-model="snackbar" :color="snackType" :timeout="4000" :multi-line="true" shaped>
        {{ snackMessage }}

        <v-btn rounded small @click="snackbar = false" :color="snackType">
            Close
        </v-btn>

    </v-snackbar>
    <v-container align="end" flex  justify='center'>

        <v-row v-if="nav[0]" align="stretch" justify='center'>
            <v-col cols="12">
            <AllHospital :key="refreshTable" />
           </v-col>
        </v-row>

        <v-row v-if="nav[1]" align="end" justify='center'> 
            <v-col cols="12">
            <AddHospital />
            </v-col>
        </v-row>

        <v-row align="stretch"  justify='center'>
            <v-col class="text-center">
                <div>
                    <v-bottom-navigation v-model="bottomNav" background-color='green' shift grow @change="botton_nav">
                        <v-btn @click="nav= [1,0,0]">
                            <span>All Hospitals</span>
                            <v-icon>mdi-hospital-building</v-icon>
                        </v-btn>
                        <v-btn @click="nav= [0,1,0]">
                            <span>Add Hospital </span>
                            <v-icon>mdi-home-plus-outline</v-icon>
                        </v-btn>
                        <v-btn @click="nav= [0,0,1]">
                            <span>Edit Hospital</span>
                            <v-icon>mdi-home-edit-outline</v-icon>
                        </v-btn>
                        <v-btn @click="askRemoveHospital">
                            <span>Remove Hospital</span>
                            <v-icon>mdi-home-remove-outline</v-icon>
                        </v-btn>

                        <v-chip :active="chip">
                            {{chiptxt}}
                        </v-chip>

                    </v-bottom-navigation>
                </div>
            </v-col>
        </v-row>

    </v-container>


    <v-dialog v-model="dialog" persistent max-width="500">
        <v-card>
            <v-card-title class="headline">Do you really want to delete this hospital?</v-card-title>
            <v-card-text> ID : {{this.$store.state.currentHospital._id}}<br /> Name : {{this.$store.state.currentHospital.name}}<br /> </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="green darken-1" text @click="dialog = false">No</v-btn>
                <v-btn color="green darken-1" text @click="RemoveHospital">Yes</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</div>
</template>

<script>
import AllHospital from "@/components/AllHospitals";
import AddHospital from "@/components/AddHospital";
import axios from 'axios';

export default {
    name: "Hospital",
    data() {
        return {
            nav: [1,0,0],
            bottomNav: '0',
            chip: false,
            chiptxt: '',
            dialog: false,
            snackbar: false,
            snackMessage: "",
            snackType: "error",
            errors: [],
            respData: {},
            refreshTable: true,
        }
    },
    components: {
        AllHospital,
        AddHospital,

    },
    methods: {
        botton_nav() {
            // console.log(e)
        },
        closeCurrentHospital() {
            this.chip = false
            this.$store.commit('setCurrentHospital', [])

        },
        askRemoveHospital() {

            if (this.$store.state.currentHospital._id != null) {
                this.dialog = true

            } else {
                this.snackbar = true,
                    this.snackMessage = "Nothing to delete \n select a Hospital to delete",
                    this.snackType = "warning"

            }

        },
        RemoveHospital() {
            this.dialog = false

            axios
                .post('http://127.0.0.1:5000/hospital/delete', {
                    _id: this.$store.state.currentHospital._id
                })
                .then(response => {
                    (this.respData = response.data)
                })
                .catch(err => (this.errors = err))

        }
    },

    watch: {
        '$store.state.currentHospital'() {

            if (this.$store.state.currentHospital._id != null) {
                this.chip = true
                this.chiptxt = 'Current Hospital : ' + this.$store.state.currentHospital.name
            } else {
                this.chiptxt = ''
                this.chip = false

            }
        },
        errors() {
            this.snackMessage = "Error when deleting hospital \n" + this.errors
            this.snackType = "error"
            this.snackbar = true
        },
        respData() {
            this.refreshTable = !this.refreshTable
            this.snackMessage = this.respData.resp
            this.snackType = "success"
            this.snackbar = true
            this.$store.commit('setCurrentHospital', {})


        }

    },
    //  mounted() {
    //  if (this.$route.params.id == null) {

    //      this.$router.push('/hospital/')
    //  }

    //}
}
</script>
