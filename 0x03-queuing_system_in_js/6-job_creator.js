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

const jobData = {
  phoneNumber: "1234567890",
  message: "Hello from Kue!",
};

const job = queue.create("push_notification_code", jobData);

// Event listener when job is successfully created
job.on("enqueue", () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event listener when job completes successfully
job.on("complete", () => {
  console.log("Notification job completed");
});

// Event listener when job fails
job.on("failed", () => {
  console.log("Notification job failed");
});

// Save the job to the queue
job.save((err) => {
  if (err) {
    console.error("Error creating job:", err);
  }
});
