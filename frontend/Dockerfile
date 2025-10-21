FROM node:20-bullseye

WORKDIR /app

# Copy everything inside dashboard
COPY dashboard ./

# Force a full fresh install
RUN npm cache clean --force && npm install

EXPOSE 3000
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]
