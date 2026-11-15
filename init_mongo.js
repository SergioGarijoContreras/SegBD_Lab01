db = db.getSiblingDB('admin');
db.auth(process.env.MONGO_INITDB_ROOT_USERNAME, process.env.MONGO_INITDB_ROOT_PASSWORD);
db = db.getSiblingDB(process.env.MONGO_INITDB_DATABASE);
db.createUser({
  user: process.env.MONGO_APP_USERNAME,
  pwd: process.env.MONGO_APP_PASSWORD,
  roles: [{ role: "read", db: process.env.MONGO_INITDB_DATABASE }]
});
db.usuarios.insertOne({ username: "alice", password: "UNIR_SegBD_Lab01" });
