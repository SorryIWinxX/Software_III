package com.example.demosender.consumer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;
@Component
public class Consumer {

    private static final Logger log = LoggerFactory.getLogger(Consumer.class);

    @RabbitListener(queues = { "${example.queue.name}"})
    public void receive(@Payload String message){
        log.info("Received message {}", message);
        makeSlow();
    }

    private void makeSlow() {

        try{
            Thread.sleep(5000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }

}
