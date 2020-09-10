<template>
  <v-app>
    <v-app-bar
      app
      flat
      color="#f2eace"
    >
      <div class="d-flex align-center">
        <h2>すうじ⇄かんすうじ。</h2>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/tomoohive/alter"
        target="_blank"
        text
      >
        <span class="mr-2">GITHUB</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <Conversion/>
    </v-main>
  </v-app>
</template>

<script>
import Conversion from './components/Conversion';

export default {
  name: 'App',

  components: {
    Conversion,
  },

  data: () => ({
    //
  }),
};
</script>
