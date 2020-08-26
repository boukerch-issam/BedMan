import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user:{
      name:"su",
      isAuthenticated:true,
      role:"su"
    },
    currentHospital:{}
  },
  getters:{
    getCurrentHospital(state){
      return "state.currentHospital"
    }
  },
  mutations: {
    setCurrentHospital(state, payload){
      state.currentHospital=payload
    },
    clearCurrentHospital(state){
      state.currentHospital={}
    }

  },
  actions: {},
  modules: {}
});
