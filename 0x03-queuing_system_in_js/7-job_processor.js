#!/usr/bin/node
/**
 * Writing the job creation function
 */
import kue from "kue";

const blacklistedPhoneNumbers = ["4153518780", "4153518781"];

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

function sendNotification(phoneNumber, message, job, done) {
  const total = 100;
  function next(per) {
    if (per === 0 || per === total / 2) {
      job.progress(per, total);
      if (per === total / 2) {
        console.log(`Sending notification to ${phoneNumber}: ${message}`);
        done();
      }
    }
    if (blacklistedPhoneNumbers.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    if (per === total) {
      done();
    }
  }
  return next(0);
}

queue.process("push_notification_code_2", 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
