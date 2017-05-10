const Koa = require('koa');

const bodyParser = require('koa-bodyparser');

const serve = require('koa-static');

const controller = require('./controller');

const templating = require('./templating');

const rest = require('./rest');

const app = new Koa();

const http = require('http')

// log request URL:
app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}...`);
    await next();
});

// static server:
app.use(serve(__dirname + '/static'));

// parse request body:
app.use(bodyParser());

// add nunjucks as view:
app.use(templating('views', {
    noCache: true,
    watch: true
}));

// bind .rest() for ctx:
app.use(rest.restify());

// add controllers:
app.use(controller());

app.listen(8888);

http.get('http://127.0.0.1:3000/api/ip')

console.log('app started at port 8888...');
