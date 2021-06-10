FROM golang:alpine

WORKDIR /go/src/app

COPY . .

RUN go mod init github.com/turnes/CloudNativeFundamentals-nd064_course_1/tree/main/exercises/go-helloworld \
    && go build -o helloworld

EXPOSE 6111
CMD [ "./helloworld" ]
