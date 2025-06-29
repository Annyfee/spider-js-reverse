require('./env')
require('./loader')
require('./mod02') // 这个的执行顺序的前后也需要注意
require('./mod01')

let a = window.loader(19)  // 19这里点开loader，发现是个自执行，啥都没有(希望的19)。需要我们再引入一个mod

// nonce = t

function get_all(account, password) {
    function get_account() {
        return (0, a.getEncryptPwd)(account)
    }
    function get_pwd() {
        return (0, a.getEncryptPwd)(password)
    }
    return {
        account:get_account(),
        pwd:get_pwd(),
    }
}

act = process.argv[2]
pwd = process.argv[3]
const ret = get_all(act,pwd)
res = JSON.stringify(ret)
console.log(res)

// let {nonce,account,pwd,signature} = process.argv[2]
// nonce,account,pwd,signature = get_all(nonce,account,pwd,signature)
// // console.log(nonce,account,pwd,signature)

process.exit()

// const {nonce,account,pwd,signature} = get_all('123456789','123456')

// console.log('nonce:::',nonce)
// console.log('account:::',account)
// console.log('pwd:::',pwd)
// console.log('signature:::',signature)