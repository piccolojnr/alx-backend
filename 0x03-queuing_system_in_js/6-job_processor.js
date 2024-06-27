#!/usr/bin/node
/**
 * Writing the job creation function
 */
import kue from "kue";

const redisConfig = {
  redis: {
    port: 6379,
    host: "127.0.0.1", // Redis server host
  },
};
const queue = kue.createQueue(redisConfig);

queue.on("ready", () => {
  console.log("Kue connected to Redis");
});

queue.on("error", (err) => {
  console.error("Error connecting to Redis: ", err);
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}: ${message}`);
}

queue.process("push_notification_code", (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
