<template>
<v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
        <v-list dense>
            <v-list-item to = "/" link>
                <v-list-item-action>
                    <v-icon>mdi-home</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Home</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item to = "/dashboard" link>
                <v-list-item-action>
                    <v-icon>mdi-view-dashboard-variant</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Dashboard</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item to = "/hospital"  link>
                <v-list-item-action>
                    <v-icon>mdi-domain</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Hospital</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
            <v-list-item to = "/about" link>
                <v-list-item-action>
                    <v-icon>mdi-information-variant</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>About</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="indigo" dark>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Bed MAN</v-toolbar-title>
    </v-app-bar>

    <v-main>
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-col class="text-center">
                    <router-view></router-view>
                </v-col>
            </v-row>
        </v-container>

    </v-main>
    <v-footer color="indigo" app>
        <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
</v-app>
</template>

<script>


export default {
    name: "App",

    props: {
        source: String,
    },
    data: () => ({
        drawer: null,
    }),
}
</script>
