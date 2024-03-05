const { MongoClient } = require('mongodb');

// Connection URI
const uri = 'mongodb://localhost:27017/cube-test';

// Create a MongoDB client
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function run() {
  try {
    // Connect to the MongoDB server
    await client.connect();
    console.log('Connected to the database');

    // Specify the database
    const database = client.db('cube-test');

    // Insert data into collections
    await insertDataIntoCollection(database, 'branch', [
      { branch_name: 'Brighton', branch_city: 'Brooklyn', assets: 7100000 },
      { branch_name: 'Downtown', branch_city: 'Brooklyn', assets: 9000000 },
      { branch_name: 'Mianus', branch_city: 'Horseneck', assets: 400000 },
      { branch_name: 'North Town', branch_city: 'Rye', assets: 3700000 },
      { branch_name: 'Perryridge', branch_city: 'Horseneck', assets: 1700000 },
      { branch_name: 'Pownal', branch_city: 'Bennington', assets: 300000 },
      { branch_name: 'Redwood', branch_city: 'Palo Alto', assets: 2100000 },
      { branch_name: 'Round Hill', branch_city: 'Horseneck', assets: 8000000 }
    ]);

    await insertDataIntoCollection(database, 'customer', [
      { customer_name: 'Adams', customer_street: 'Spring', customer_city: 'Pittsfield' },
      { customer_name: 'Brooks', customer_street: 'Senator', customer_city: 'Brooklyn' },
      { customer_name: 'Curry', customer_street: 'North', customer_city: 'Rye' },
      { customer_name: 'Glenn', customer_street: 'Sand Hill', customer_city: 'Woodside' },
      { customer_name: 'Green', customer_street: 'Walnut', customer_city: 'Stamford' },
      { customer_name: 'Hayes', customer_street: 'Main', customer_city: 'Harrison' },
      { customer_name: 'Johnson', customer_street: 'Alma', customer_city: 'Palo Alto' },
      { customer_name: 'Jones', customer_street: 'Main', customer_city: 'Harrison' },
      { customer_name: 'Lindsay', customer_street: 'Park', customer_city: 'Pittsfield' },
      { customer_name: 'Smith', customer_street: 'North', customer_city: 'Rye' },
      { customer_name: 'Turner', customer_street: 'Putnam', customer_city: 'Stamford' },
      { customer_name: 'Williams', customer_street: 'Nassau', customer_city: 'Princeton' }
    ]);

    await insertDataIntoCollection(database, 'loan', [
      { loan_number: 'L-11', branch_name: 'Round Hill', amount: 900 },
      { loan_number: 'L-14', branch_name: 'Downtown', amount: 1500 },
      { loan_number: 'L-15', branch_name: 'Perryridge', amount: 1500 },
      { loan_number: 'L-16', branch_name: 'Perryridge', amount: 1300 },
      { loan_number: 'L-17', branch_name: 'Downtown', amount: 1000 },
      { loan_number: 'L-23', branch_name: 'Redwood', amount: 2000 },
      { loan_number: 'L-93', branch_name: 'Mianus', amount: 500 }
    ]);

    await insertDataIntoCollection(database, 'account', [
      { account_number: 'A-101', branch_name: 'Downtown', balance: 500 },
      { account_number: 'A-102', branch_name: 'Perryridge', balance: 400 },
      { account_number: 'A-201', branch_name: 'Brighton', balance: 900 },
      { account_number: 'A-215', branch_name: 'Mianus', balance: 700 },
      { account_number: 'A-217', branch_name: 'Brighton', balance: 750 },
      { account_number: 'A-222', branch_name: 'Redwood', balance: 700 },
      { account_number: 'A-305', branch_name: 'Round Hill', balance: 350 }
    ]);

    await insertDataIntoCollection(database, 'depositor', [
      { customer_name: 'Hayes', account_number: 'A-102' },
      { customer_name: 'Johnson', account_number: 'A-101' },
      { customer_name: 'Johnson', account_number: 'A-201' },
      { customer_name: 'Jones', account_number: 'A-217' },
      { customer_name: 'Lindsay', account_number: 'A-222' },
      { customer_name: 'Smith', account_number: 'A-215' },
      { customer_name: 'Turner', account_number: 'A-305' }
    ]);

    await insertDataIntoCollection(database, 'borrower', [
      { customer_name: 'Adams', loan_number: 'L-16' },
      { customer_name: 'Curry', loan_number: 'L-93' },
      { customer_name: 'Hayes', loan_number: 'L-15' },
      { customer_name: 'Johnson', loan_number: 'L-14' },
      { customer_name: 'Jones', loan_number: 'L-17' },
      { customer_name: 'Smith', loan_number: 'L-11' },
      { customer_name: 'Smith', loan_number: 'L-23' },
      { customer_name: 'Williams', loan_number: 'L-17' }
    ]);

  } finally {
    // Close the connection
    await client.close();
    console.log('Connection closed');
  }
}

async function insertDataIntoCollection(database, collectionName, data) {
  const collection = database.collection(collectionName);
  await collection.insertMany(data);
  console.log(`${data.length} documents inserted into ${collectionName} collection`);
}

// Run the code
run().catch(console.error);
