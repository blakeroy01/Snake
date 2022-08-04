# First, specify the language it needs to run on
FROM golang:1.18

# Set the Working Directory
WORKDIR /app

# Copy our instructions for dependencies
COPY go.mod ./
COPY go.sum ./

# Download dependencies
RUN go mod download

# Copy the server code
COPY ./ ./

# Build the server as a binary (this mnakes it run way faster than using go run ...)
RUN go build cmd/main.go

# Tell Docker what to run when it starts up
CMD [ "./main" ]