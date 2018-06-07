// 'use strict';

const gulp 			= require('gulp');
const gulpCopy		= require('gulp-copy');
const plumber		= require('gulp-plumber');
const sass 			= require('gulp-sass');
const uglify 		= require('gulp-uglify');
const babel			= require('gulp-babel');
const watch 		= require('gulp-watch');
const concat		= require('gulp-concat');
const minifyCss		= require('gulp-minify-css');
const autoprefixer	= require('gulp-autoprefixer');
const livereload	= require('gulp-livereload');
const soursemaps	= require('gulp-sourcemaps');

// FILE PATH
const _scripts_path = 'src/js/**/*.js';
const _HTML_path 	= 'src/*.html';
const _sass_path	= 'src/scss/**/*.scss'
const _dist_path	= 'dist/'
const _images_path  = 'src/img/*'		

gulp.task('copy', () => {
	console.log('Starting COPY task')
	return gulp.src(_HTML_path)
		.pipe(gulpCopy(_dist_path, {prefix: 1}))
		.pipe(livereload())
});

gulp.task('copy_images', () => {
	console.log('STARTING COPY_IMAGES TASK..')
	
	return gulp.src(_images_path)
		.pipe(gulpCopy(_dist_path, {prefix: 1}))
		.pipe(livereload())
});

// Move fonts folder to dist
gulp.task('fa-copy', () => {
	return gulp.src('node_modules/font-awesome/fonts/*')
		.pipe(gulp.dest(_dist_path + 'fonts/'))
})

// Move fontawesome css to dist
gulp.task('fa-css', () => {
	return gulp.src('node_modules/font-awesome/css/font-awesome.min.css')
		.pipe(gulp.dest(_dist_path + 'css/'))
})


gulp.task('sass', () => {
	console.log('Starting SASS task')
	return gulp.src (['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/styles.scss'])
		.pipe(plumber( function (err) {
			console.log('SASS task error');
			console.log(err);
			this.emit('end')
		}))
		.pipe(soursemaps.init())
		.pipe(autoprefixer())
		.pipe(sass({
			outputStyle: 'compressed'
		}))
		.pipe(soursemaps.write())
		.pipe(gulp.dest(_dist_path + 'css/'))
		.pipe(livereload())
});

gulp.task('sass:watch', () => {
	gulp.watch('src/sass/**/*.scss', ['sass']);
});

gulp.task('copy-js', () => {
	console.log('copying bootstrap js from node_modules')
	return gulp.src (['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/popper.js/dist/umd/popper.min.js', 'node_modules/knockout/build/output/knockout-latest.js'])
		.pipe(gulp.dest('dist/js'))
		.pipe(livereload())
});

gulp.task('scripts', () => {
	console.log('Starting SCRIPTS task')
	return gulp.src(_scripts_path)
		.pipe(plumber( function(err) {
			console.log('SCRIPTS task error');
			console.log(err);
			this.emit('end')
		}))
		.pipe(soursemaps.init())
		.pipe(babel({
			presets: ['es2015']
		}))
		.pipe(uglify().on('error', (e) => {
			console.log(e)
		}))
		.pipe(concat('main.js'))
		.pipe(soursemaps.write())
		.pipe(gulp.dest('dist/js'))
		.pipe(livereload())
})

gulp.task('default', ['copy','copy-js', 'fa-copy', 'fa-css', 'copy_images','scripts', 'sass'],() => {
	console.log('Starting DEFAULT task')
})

gulp.task('server', ['default'],() => {
	console.log('Starting WATCH task')
	require('./server.js')
	livereload.listen(35729);
	gulp.watch(_HTML_path, ['copy'])
	gulp.watch(_images_path, ['copy_images'])
	gulp.watch(_scripts_path, ['scripts'])
	gulp.watch(_sass_path, ['sass'])
});













