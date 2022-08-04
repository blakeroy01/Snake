package cache

import (
	"context"
	"fmt"

	"github.com/go-redis/redis/v8"
)

var (
	ctx = context.Background()
)

// Initialize returns a Redis Client that can interact with a running redis server.
func Initalize(address string, password string, database int) (*redis.Client, error) {
	redisClient := redis.NewClient(&redis.Options{
		Addr:     address,
		Password: password,
		DB:       database,
	})

	pong, err := redisClient.Ping(ctx).Result()
	fmt.Println(pong)
	if err != nil {
		return nil, err
	}

	return redisClient, err
}
