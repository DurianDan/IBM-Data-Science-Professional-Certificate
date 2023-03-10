const http = require("http");

function JSONfromBuffer(chunk){
    return JSON.parse(chunk.toString())
}

const server = http.createServer((req,res)=>{
    if (req.method == "POST"){
        let body = {};
        req.on('data', chunk => {
            body = JSONfromBuffer(chunk); // convert Buffer to string
        });
        req.on('end', () => {
            console.log(body[1]);
            res.end('ok');
        });
        
    }
    else {
        res.end(`
          <!doctype html>
          <html>
          <body>
              <form action="/" method="post">
                  <input type="text" name="fname" /><br />
                  <input type="number" name="age" /><br />
                  <input type="file" name="photo" /><br />
                  <button>Save</button>
              </form>
          </body>
          </html>
        `);
      }
})

server.listen(5000)