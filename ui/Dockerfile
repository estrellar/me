#build js
FROM node:latest as ui
WORKDIR /usr/src/app
COPY package.json ./
RUN npm install
COPY . .

#serve nginx
FROM nginx:latest
COPY --from=ui /usr/src/app/dist/ui /usr/share/nginx/html
EXPOSE 80
