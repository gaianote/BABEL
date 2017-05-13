const model = require('../model');
const APIError = require('../rest').APIError;
const request = require('request')

const Ip = model.Ip


module.exports = {
    'GET /api/ip': async (ctx, next) => {
      const options = {
        headers: {"Connection": "close"},
          url: 'http://127.0.0.1:8888',
          method: 'PUT',
          json:true,
          body: {'host':'171.11.108.82000','token':'2577dcd0-2bee-450f-84a3-a87487bd0427'}
      };
      request(options, (error, response, data)=>{
        if (!error && response.statusCode == 200) {
          const getdata = () => { return data }
        }
      });

      console.log(getdata())
    },
    'POST /api/ip': async (ctx, next) => {
      const token = ctx.request.body.token
      const host = ctx.request.body.host
      if(token === '2577dcd0-2bee-450f-84a3-a87487bd0427'){
        ip = await Ip.create({'ip': ctx.ip,'host':host});
        console.log(ip.get({'plain': true}))
      }
    },
    'PUT /api/ip': async (ctx, next) => {
      const token = ctx.request.body.token
      const host = ctx.request.body.host
      if(token === '2577dcd0-2bee-450f-84a3-a87487bd0427'){
        let ip = await Ip.findOne({'where': {'host':host}});
        ip = await ip.update({'ip':ctx.ip})
        console.log(ip.get({'plain': true}).ip)
      }
    }
};