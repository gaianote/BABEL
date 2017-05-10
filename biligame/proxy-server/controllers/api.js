const model = require('../model');
const APIError = require('../rest').APIError;
const ip = require('ip')

module.exports = {
  'GET /api/ip': async (ctx, next) => {
        shell.exec('pppoe-stop')
        shell.exec('pppoe-start')
        ctx.rest({'ip':ip.address()})
        shell.echo(ip.address())
    },
};
