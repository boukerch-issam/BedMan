<template>
<div>
<v-snackbar v-model="snackbar" :color="snackType" :timeout="-1" :multi-line="true" shaped>
    {{ snackMessage }}

    <v-btn rounded small @click="snackMan" :color="snackType">
        Close
    </v-btn>

</v-snackbar>
<v-card elevation=12 >

    <v-form ref="form" @submit.prevent="submit">
        <v-container fluid>
            <v-row>
                <v-col cols="12">
                    <v-text-field v-model="form.Name" :rules="rules.name" color="purple darken-2" outlined label="Hospital Name" hint="Mustapha Bacha" required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <v-text-field v-model="form.Code" :rules="rules.name" color="blue darken-2" outlined label="Hospital Code" hint="16-01" required></v-text-field>
                </v-col>
                <v-col cols="12">
                    <v-textarea v-model="form.Description" outlined color="teal">
                        <template v-slot:label>
                            <div>
                                Description <small>(optional)</small>
                            </div>
                        </template>
                    </v-textarea>
                </v-col>
                <v-col cols="12">
                    <v-checkbox v-model="form.terms" color="green">
                        <template v-slot:label>
                            <div @click.stop="">
                                Are you sure to add this hospital according to these
                                <a href="javascript:;" @click.stop="terms = true">terms</a>
                            </div>
                        </template>
                    </v-checkbox>
                </v-col>
            </v-row>
        </v-container>
        <v-card-actions>
            <v-btn text @click="resetForm">Cancel</v-btn>
            <v-spacer></v-spacer>
            <v-btn :disabled="!formIsValid" text color="primary" type="submit">Register</v-btn>
        </v-card-actions>
    </v-form>
    <v-dialog v-model="terms" width="70%">
        <v-card>
            <v-card-title class="title">Terms</v-card-title>
            <v-card-text>
                {{ content }}
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn text color="purple" @click="terms = false">Ok</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</v-card>
</div>
</template>

<script>
import axios from 'axios';
export default {
    data() {

        const defaultForm = Object.freeze({
            Name: '',
            Code: '',
            Description: '',
            terms: false,
        })

        return {
            form: Object.assign({}, defaultForm),
            rules: {

                name: [val => (val || '').length > 0 || 'This field is required'],
            },

            content: 'these are the terms to add a hospital',
            snackbar: false,
            snackMessage: "",
            snackType: "error",
            terms: false,
            defaultForm,
            respData: null,
            error: null,
        }
    },

    computed: {
        formIsValid() {
            return (
                this.form.Name &&
                this.form.Code &&
                this.form.terms
            )
        },
    },

    methods: {
        snackMan() {
            this.snackbar = false
            this.error = null
            this.respData = null
        },
        resetForm() {
            this.form = Object.assign({}, this.defaultForm)
            this.$refs.form.reset()
        },
        submit() {
            axios
                .post('http://127.0.0.1:5000/hospital/add', {
                    code: this.form.Code,
                    name: this.form.Name,
                    position: '',
                    description: this.form.Description,

                })
                .then(response => {
                    (this.respData = response.data)
                })
                .catch(err => (this.error = err))

            this.resetForm()
        },
    },
    watch: {
        error() {
            if (this.error != null) {
                this.snackbar = true
                this.snackMessage = "Error when adding \n name or code may be used!!"
                this.snackType = "error"
            }

        },
        respData() {
            if (this.respData != null) {
                this.snackbar = true
                this.snackMessage = "Hospital added successfully with the  ID \n" + this.respData._id
                this.snackType = "success"
            }

        }

    },
}
</script>
