<template lang="pug">
div.centering_parent.cream
  div.centering_item
    div(style="margin: 0px 10%")
      v-text-field(label="兆の桁以下で入力してください。" single-line solo v-model="InputText" background-color="#f2eace")
      div(style="margin: 0px 0px 0px 0px")
        v-btn(small color="error" @click="SendtoApi") CHANGE
      v-card(class="mx-auto" style="margin: 40px 0px; padding: 4px 0px" color="#f2eace")
        p(style="margin: 5px; padding: 0px 8px") {{ result }}
</template>

<script>
import axios from 'axios'
export default {
  name: 'Conversion',
  data: () => ({
    InputText: '',
    result: 'RESULT'
  }),
  methods: {
    SendtoApi: function () {
      var data = this.InputText
      if(!isNaN(data)) {
        var path1 = `/v1/number2kanji/` + data
        axios.get(path1)
        .then(response => {
          this.result = response.data.result
        })
        .catch(error => {
          console.log(error)
          alert('不正な文字列')
        })
      } else {
        var path2 = `/v1/kanji2number/` + data
        axios.get(path2)
        .then(response => {
          this.result = response.data.result
        })
        .catch(error => {
          console.log(error)
          alert('不正な文字列')
        })
      }
    }
  }
}
</script>

<style scoped>
.centering_parent {
    padding: 20px;              /* 余白指定 */
    height: 100%;              /* 高さ指定 */
}

.centering_item {
   padding: 20px;               /* 余白指定 */
   top:  0;                     /* 位置指定 */
   bottom: 0;                  /* 位置指定 */
   left:  0;                    /* 位置指定 */
   right:  0;                   /* 位置指定 */
   margin: 30% auto;               /* 中央寄せ */
}

.cream {
  background: #f2eace;
}
</style>
