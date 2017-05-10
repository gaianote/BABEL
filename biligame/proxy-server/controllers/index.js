
module.exports = {
    'GET /': async (ctx, next) => {
        console.log(`请求ip为:${ctx.ip}`)
        ctx.render('index.html');
    }
};
