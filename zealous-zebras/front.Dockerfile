FROM node:alpine as builder
WORKDIR /app
COPY . .
WORKDIR /app/timescape/frontend
RUN npm install -l --silent
EXPOSE 3000
CMD ["npm", "start"]