<template>
<div>
    <div>
        <v-data-table show-select item-key="_id" :single-select="singleSelect" v-model="selected" :headers="headers" :items="hospitalsList" :items-per-page="5" class="elevation-1"></v-data-table>
    </div>
    
    <v-snackbar  v-model="snackbar" :color="snackType" :timeout="4000" :multi-line="true" shaped >
        {{ snackMessage }}

  
            <v-btn rounded small @click="snackbar = false" :color="snackType">
                Close
            </v-btn>

    </v-snackbar>
</div>
</template>

<script>
import axios from 'axios';
export default {

    data() {
        return {
            singleSelect: true,
            selected: [],
            headers: [{
                    text: 'Name',
                    align: 'start',
                    sortable: false,
                    value: 'name',
                },

                {
                    text: 'Code',
                    value: 'code'
                },
                {
                    text: 'Position',
                    value: 'position'
                },
                {
                    text: 'Description',
                    value: 'description'
                },
                {
                    text: 'Identifier',
                    value: '_id'
                },
            ],
            hospitalsList: [],
            errors: [],
            snackbar: false,
            snackMessage: "",
            snackType: "error"
        }
    },
    mounted() {
        axios
            .get('http://127.0.0.1:5000/hospital/all')
            .then(response => (this.hospitalsList = response.data))
            .catch(err => (this.errors = err))
    },
    watch: {
        errors() {
            this.snackMessage = "Error when loading hospitals data \n" + this.errors
            this.snackType = "error"
            this.snackbar = true
        },
        hospitalsList(){
            
            this.snackMessage = "Hospitals data Loaded"
            this.snackType = "success"
            this.snackbar = true
        },
        selected(){ 
            if (this.selected[0] != null){
            this.$store.commit('setCurrentHospital',  this.selected[0])
            }else{
                this.$store.commit('setCurrentHospital',{})
            }
        },        
        // '$store.state.currentHospital'() {
            
        //     if (this.$store.state.currentHospital._id == null ){
            
        //         this.selected=[]
        //     }
        // }


    }

}
</script>
