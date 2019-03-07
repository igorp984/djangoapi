FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend/
COPY ./src /app/frontend/
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
